# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from ovos_utils.waiting_for_mycroft.base_skill import MycroftSkill, FallbackSkill
from ovos_utils.waiting_for_mycroft.common_play import CommonPlaySkill, CPSMatchType
from ovos_utils.waiting_for_mycroft.skill_gui import SkillGUI
import mycroft

mycroft.enclosure.gui.SkillGUI = SkillGUI

mycroft.skills.mycroft_skill.MycroftSkill = MycroftSkill
mycroft.skills.MycroftSkill = MycroftSkill

mycroft.skills.CommonPlaySkill = CommonPlaySkill
mycroft.skills.common_play_skill.CommonPlaySkill = CommonPlaySkill
mycroft.skills.CPSMatchType = CPSMatchType
mycroft.skills.common_play_skill.CPSMatchType = CPSMatchType

mycroft.skills.FallbackSkill = FallbackSkill
mycroft.skills.fallback_skill.FallbackSkill = FallbackSkill

from mycroft.configuration import LocalConf, USER_CONFIG


class MonkeyPatcherSkill(MycroftSkill):
    def __init__(self):
        super(MonkeyPatcherSkill, self).__init__()
        self.make_priority()

    # make priority skill in first install
    def get_intro_message(self):
        self.make_priority()
        self.speak_dialog("installed")

    def make_priority(self):
        # load the current list of already blacklisted skills
        priority_list = self.config_core["skills"]["priority_skills"]

        # add the skill to the blacklist
        if self.skill_id not in priority_list:
            priority_list.insert(0, self.skill_id)

            # load the user config file (~/.mycroft/mycroft.conf)
            conf = LocalConf(USER_CONFIG)
            if "skills" not in conf:
                conf["skills"] = {}

            # update the blacklist field
            conf["skills"]["priority_skills"] = priority_list

            # save the user config file
            conf.store()


def create_skill():
    return MonkeyPatcherSkill()
