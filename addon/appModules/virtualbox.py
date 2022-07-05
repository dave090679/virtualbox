#appModules/virtualbox.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2012 NVDA Contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
import ui
import appModuleHandler
import controlTypes
import api
from NVDAObjects.IAccessible import IAccessible
class vbox_tablerow(IAccessible):
	def _get_name(self):
		ret = ""
		l = list()
		for x in self.children:
			try:
				childname = x.name
			except:
				childname = "nicht belegt"
			if childname != None:
				l.append(childname)
			else:
				l.append("nicht belegt")
		ret = "; ".join(l)
		return ret

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.Role.TABLEROW:
			clslist.insert(0, vbox_tablerow)
