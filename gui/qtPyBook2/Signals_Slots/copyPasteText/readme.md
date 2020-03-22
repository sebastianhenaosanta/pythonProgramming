# Copying and pasting text from one Line Edit widget to another

This recipe will make you understand how an event performed on one widget invokes a
predefined action on the associated widget. Because we want to copy content from one
Line Edit widget on clicking the push button, we need to invoke the selectAll() method
on the occurrence of the pressed() event on push button. Also, we need to invoke the
copy() method on occurrence of the released() event on the push button. To paste the
content in the clipboard into another Line Edit widget on clicking of another push button,
we need to invoke the paste() method on the occurrence of the clicked() event on another
push button.
