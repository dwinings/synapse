import synapse.lib.cli as s_cli
import synapse.lib.mixins as s_mixins
import synapse.lib.reflect as s_reflect
#import synapse.cmds.cortex as s_cmds_cortex

# Add our commands to the mixins registry
s_mixins.addSynMixin('cmdr','synapse.cores.common.Cortex','synapse.cmds.cortex.AskCmd')
s_mixins.addSynMixin('cmdr','synapse.cores.common.Cortex','synapse.cmds.cortex.AddTagCmd')
s_mixins.addSynMixin('cmdr','synapse.cores.common.Cortex','synapse.cmds.cortex.DelTagCmd')
s_mixins.addSynMixin('cmdr','synapse.cores.common.Cortex','synapse.cmds.cortex.AddNodeCmd')


def getItemCmdr(item, outp=None, **opts):

    cmdr = s_cli.Cli(item,outp=outp)

    refl = s_reflect.getItemInfo(item)
    if refl == None:
        return cmdr

    for name in refl.get('inherits',()):
        for mixi in s_mixins.getSynMixins('cmdr',name):
            cmdr.addCmdClass(mixi)

    return cmdr