# canonical.py - functions for converting systems to canonical forms
# RMM, 10 Nov 2012

from control.exception import ControlNotImplemented
from control.lti import issiso
from control.statesp import StateSpace
from control.statefbk import ctrb, obsv

from numpy import zeros, shape, poly
from numpy.linalg import solve, matrix_rank, inv

__all__ = ['canonical_form', 'reachable_form', 'observable_form']

def canonical_form(xsys, form='reachable'):
    """Convert a system into canonical form
    Parameters
    ----------
    xsys : StateSpace object
        System to be transformed, with state 'x'
    form : String
        Canonical form for transformation.  Chosen from:
          * 'reachable' - reachable canonical form
          * 'observable' - observable canonical form
          * 'modal' - modal canonical form [not implemented]
    Returns
    -------
    zsys : StateSpace object
        System in desired canonical form, with state 'z'
    T : matrix
        Coordinate transformation matrix, z = T * x
    """

    # Call the appropriate tranformation function
    if form == 'reachable':
        return reachable_form(xsys)
    elif form == 'observable':
        return observable_form(xsys)
    else:
        raise ControlNotImplemented(
            "Canonical form '%s' not yet implemented" % form)


# Reachable canonical form
def reachable_form(xsys):
    """Convert a system into reachable canonical form
    Parameters
    ----------
    xsys : StateSpace object
        System to be transformed, with state `x`
    Returns
    -------
    zsys : StateSpace object
        System in reachable canonical form, with state `z`
    T : matrix
        Coordinate transformation: z = T * x
    """
    # Check to make sure we have a SISO system
    if not issiso(xsys):
        raise ControlNotImplemented(
            "Canonical forms for MIMO systems not yet supported")

    # Create a new system, starting with a copy of the old one
    zsys = StateSpace(xsys)

    # Generate the system matrices for the desired canonical form
    zsys.B = zeros(shape(xsys.B))
    zsys.B[0, 0] = 1.0
    zsys.A = zeros(shape(xsys.A))
    Apoly = poly(xsys.A)                # characteristic polynomial
    for i in range(0, xsys.states):
        zsys.A[0, i] = -Apoly[i+1] / Apoly[0]
        if (i+1 < xsys.states):
            zsys.A[i+1, i] = 1.0

    # Compute the reachability matrices for each set of states
    Wrx = ctrb(xsys.A, xsys.B)
    Wrz = ctrb(zsys.A, zsys.B)

    if matrix_rank(Wrx) != xsys.states:
        raise ValueError("System not controllable to working precision.")

    # Transformation from one form to another
    Tzx = solve(Wrx.T, Wrz.T).T  # matrix right division, Tzx = Wrz * inv(Wrx)

    if matrix_rank(Tzx) != xsys.states:
        raise ValueError("Transformation matrix singular to working precision.")

    # Finally, compute the output matrix
    zsys.C = solve(Tzx.T, xsys.C.T).T  # matrix right division, zsys.C = xsys.C * inv(Tzx)

    return zsys, Tzx


def observable_form(xsys):
    """Convert a system into observable canonical form
    Parameters
    ----------
    xsys : StateSpace object
        System to be transformed, with state `x`
    Returns
    -------
    zsys : StateSpace object
        System in observable canonical form, with state `z`
    T : matrix
        Coordinate transformation: z = T * x
    """
    # Check to make sure we have a SISO system
    if not issiso(xsys):
        raise ControlNotImplemented(
            "Canonical forms for MIMO systems not yet supported")

    # Create a new system, starting with a copy of the old one
    zsys = StateSpace(xsys)

    # Generate the system matrices for the desired canonical form
    zsys.C = zeros(shape(xsys.C))
    zsys.C[0, 0] = 1
    zsys.A = zeros(shape(xsys.A))
    Apoly = poly(xsys.A)                # characteristic polynomial
    for i in range(0, xsys.states):
        zsys.A[i, 0] = -Apoly[i+1] / Apoly[0]
        if (i+1 < xsys.states):
            zsys.A[i, i+1] = 1

    # Compute the observability matrices for each set of states
    Wrx = obsv(xsys.A, xsys.C)
    Wrz = obsv(zsys.A, zsys.C)

    # Transformation from one form to another
    Tzx = inv(Wrz) * Wrx

    # Finally, compute the output matrix
    zsys.B = Tzx * xsys.B

    return zsys, Tzx
