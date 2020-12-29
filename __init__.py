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
from ovos_utils.skills import make_priority_skill
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


class MonkeyPatcherSkill(MycroftSkill):
    def __init__(self):
        super(MonkeyPatcherSkill, self).__init__()
        make_priority_skill(self.skill_id)


def create_skill():
    return MonkeyPatcherSkill()
