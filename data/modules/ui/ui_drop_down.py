from data.modules.ui.ui_element import UIElement,UIC
from pygame import Surface, Rect
from data.modules.ui.ui_button import UIButton
from data.modules.vector import Vector4
class UIDropDown(UIElement):
    """
    .. child_instances:: 
    
        list[tuple[str,callback]] Child Buttons
    .. mother_instance_button:: 
    
        The Main Button

    UX OPTIONS
    -----
    .. size:: the size of all buttons in this element
    .. text:: The text of the ``mother_instance_button``
    .. tcg:: ``#484848`` ``#a6a6a6`` ``#ffffff``
    .. bcg:: ``#777777``
    """
    def __init__(self, vector:Vector4, **kwargs) -> None:
        super().__init__(vector, **kwargs)
        self.set_image(Surface((1,1)))
        UIC.add_element('uiDropDown')
        self.toggle = False
        ux = kwargs.get('ux',{})
        if not 'tcg' in ux:
            ux['tcg'] = ux.get('tcg',('#484848','#a6a6a6','#ffffff'))
        if not 'bcg' in ux:
            ux['bcg'] = ux.get('bcg',('#777777',))
        self.mother_instance_button = UIButton(vector,ux=ux,cb_on_press=self.switch,layer=self.layer,parent=self.parent,group=self.group)
        self.child_instances = []
        
        vector.x = 0
        vector.y = 0
        self._callbacks = []
        for text,callback in kwargs.get('childs_instances',[]):
            
            ux['text'] = text
            vector.y += 24
            UIB = UIButton(vector,ux=ux,cb_on_press=self.btnPress,parent=self,layer=self.layer,group=self.group)
            self.child_instances.append(UIB)
            self._callbacks.append((callback,UIB.element_id))
        for e in self.child_instances:
            
            e.visible = False
    def btnPress(self,*_):
       
        for callback,id in self._callbacks:
            if id == _[0].element_id:
                _[0].this_frame_pressed = False
                callback(_[0])
                break
        self.toggle = False
        for e in self.child_instances:
           
            e.visible = self.toggle
    def switch(self,*_):
        self.toggle = not self.toggle
        for e in self.child_instances:
           
            e.visible = self.toggle

    def update(self):
        return super().update()
