"""
This example writes to the screen directly using Tkinter.

The local time is read and is written direct to the Tkinter canvas that is used by
Pi Presents to display its output.

"""

import time
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,Gdk
from pp_gtkutils import CSS

class krt_time(object):

    def __init__(self,root,canvas,plugin_params,track_params,show_params,pp_dir,pp_home,pp_profile):
        # called when a player is executed for a track
        self.root=root
        self.canvas=canvas
        self.plugin_params=plugin_params
        self.track_params=track_params
        self.show_params=show_params
        self.pp_dir=pp_dir
        self.pp_home=pp_home
        self.pp_profile=pp_profile
        self.css=CSS()
        # plugin must keep track of the GTK4 objects it creates.
        self.plugin_objects=[]

    def load(self,track_file,liveshow,track_type):
        # Called in advance, while the previous track is being shown.
        # called after all other track objects are loaded so these objects appear on top
        # Can do three things:
        # a. modify the track file or track file name that is about to be  loaded
        #   must return the track file whether modified, replaced  or unaltered
        # return 'normal' if no error encountered, otherwise return 'error'
        return 'normal','',track_file



    def show(self):
        #  Draw objects direct to the screen setting their state
        #  to 'normal' so they are dislayed
        #
        #  Determine whether drawing to the screen should happen repeatedly
        #  in the track by calling the redraw method
        #   = 0  do not redraw
        #   > 0 redraw at intervals (mS.)
        #  return the above value

        time_text='My Local Time at the start is: ' + time.asctime()
        plugin_obj1=Gtk.Label()
        plugin_obj1.set_label(time_text)
        plugin_obj1.set_justify(CSS.justify_map['left'])
        plugin_obj1.set_name('plugin_obj1')
        #could use other CSS statements here but replace - with _ e.g background_colour not background-colour
        self.css.style_widget(plugin_obj1,'plugin_obj1',color = 'red',font = 'bold 20pt arial')
        self.canvas.put(plugin_obj1,100,500)
        plugin_obj1.set_visible(True)
        # store object so hide() can remove it.
        self.plugin_objects.append(plugin_obj1)
        
        time_text='My Local Time now is: ' + time.asctime()        
        # this one is updated, the previos one is not 
        plugin_obj2=Gtk.Label()
        plugin_obj2.set_label(time_text)
        plugin_obj2.set_justify(CSS.justify_map['left'])
        plugin_obj2.set_name('plugin_obj2')
        #could use other CSS statements here but replace - with _ e.g background_colour not background-colour
        self.css.style_widget(plugin_obj2,'plugin_obj2',color = 'green',font = 'bold 20pt arial')
        self.canvas.put(plugin_obj2,100,600)
        plugin_obj2.set_visible(True)
        self.plugin_objects.append(plugin_obj2)
        
        # return the interval to redraw
        return 500


    def redraw(self):
        # update the text of the second object with the latest time
        time_text='My Local Time now is: ' + time.asctime()
        # index is 1 as lists start at 0
        self.plugin_objects[1].set_label(time_text)
    

    def hide(self):
        # called at ready_callback to delete the previous track's plugin objects
        # this is done on another instance of the plugin
        for plugin_object in self.plugin_objects:
                plugin_object.set_visible(False)



