# <img src='./desktop/icon/monkey_patch.png' card_color='#22a7f0' width='50' height='50' style='vertical-align:bottom'/> Monkey Patcher

Applies patches to mycroft-core at runtime

## About

Contributing to Mycroft is a bit of a fight with upstream

this skill applies a bunch of monkey patches at runtime to add/fix things 
not merged into mycroft-core, full details in [ovos_utils PR#15)](https://github.com/OpenVoiceOS/ovos_utils/pull/15)

### Patches

`MycroftSkill` and `FallbackSkill` patches:

- add `MycroftSkill.handle_skill_deactivated` from https://github.com/MycroftAI/mycroft-core/pull/1468 (improved)
- patch `MycroftSkill.bind`
    - enable `SkillApi` from https://github.com/MycroftAI/mycroft-core/pull/1822
    - enable `ovos_utils.intents.ConverseTracker`
- patch `MycroftSkill.voc_match` https://github.com/MycroftAI/mycroft-core/pull/2675
- patch `MycroftSkill.gui` to use patched `SkillGUI` (see bellow)
- patch `MycroftSkill.init_dialog` to use `ovos_utils.lang.get_language_dir`
- patch `MycroftSkill.load_vocab_files` to use `ovos_utils.lang.get_language_dir`
- patch `MycroftSkill.load_regex_files` to use `ovos_utils.lang.get_language_dir`


`SkillGUI` patches:

Video playback from https://github.com/MycroftAI/mycroft-core/pull/2683
- add `SkillGUI.play_video`
- add `SkillGUI.is_video_displayed`
- add `SkillGUI.playback_status`
- add `SkillGUI.pause_video`
- add `SkillGUI.resume_video`
- add `SkillGUI.stop_video`

Skill settings from https://github.com/MycroftAI/mycroft-core/pull/2698
- add `SkillGUI.register_settings`
- add `SkillGUI.show_settings`

`CommonPlaySkill` patches:
- add `CPSMatchType` from https://github.com/MycroftAI/mycroft-core/pull/2660

## Credits
JarbasAI

## Category
**Configuration**

## Tags
#patch
#monkey-patch
