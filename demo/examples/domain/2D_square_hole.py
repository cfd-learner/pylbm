# Authors:
#     Loic Gouarin <loic.gouarin@math.u-psud.fr>
#     Benjamin Graille <benjamin.graille@math.u-psud.fr>
#
# License: BSD 3 clause

"""
Example of a square in 2D with a circular hole
"""
import pyLBM
dico = {
    'box':{'x': [0, 1], 'y': [0, 1], 'label':0},
    'elements':[pyLBM.Circle((0.5,0.5), 0.2, label = 1)],
    'space_step':0.05,
    'schemes':[{'velocities':range(13)}],
}
dom = pyLBM.Domain(dico)
#dom.visualize(opt=0)
dom.visualize(opt=1)
dom.visualize(pyLBM.viewer.VispyViewer, opt=1)
#pyLBM.domain.verification(dom, with_color = True)
