#appModules/virtualbox.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2012 NVDA Contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
import ui
import appModuleHandler
import controlTypes
import api
from NVDAObjects.UIA import UIA, ListItem
class VBoxList(UIA):
	def event_UIA_elementSelected(self):
		for child in self.children:
			if controlTypes.State.SELECTED in child.states:
				child.setFocus()
				ui.message(child.name)
	def _get_focusRedirect(self):
		for child in self.children:
			if controlTypes.State.SELECTED in child.states:
				ui.message(child.name)
				return child
		return None
class VBoxListItem(ListItem):
	def event_gainFocus(self):
		if controlTypes.State.SELECTED in self.states:
			self.setFocus()

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.Role.LIST:
			clslist.insert(0, VBoxList)
		elif obj.role == controlTypes.Role.LISTITEM:
			clslist.insert(0, VBoxListItem)