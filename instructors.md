# Instructors

- Please see our [instructor repository](https://github.com/fredhutchio/instructors) for general guidelines relevant to all classes. Additional recommendations specific for this course can be found below.
- You may choose to share your notebook to Dropbox to help folks stay on track. If you create the project in Dropbox, you can copy the link to each class's notebook and share in HackMD. Learners will need to follow the instructions in HackMD to download the script. You may also render the notebook for them using [nbviewer](https://nbviewer.jupyter.org), but this tends to be slower to update upon saving and takes more time to setup.
- Administering challenges: Typing the challenge exercise into the notebook as a comment or separate markdown cell is usually easiest. Some challenges that include a chunk of code may be added to the HackMD for learners to copy and paste.
- It's not strictly necessary to get through all material listed for a given class. The only exception to this is class 3, as the datasets filtered for missing data, etc are used in class 4 for plotting. If you don't get through all this material, you can explain the basic methods for filtering (referring to the teaching notes if anyone wants to see the code), and have learners download the filtered data as follows:

```
import urllib.request
urllib.request.urlretrieve("https://raw.githubusercontent.com/fredhutchio/python_intro/master/extra/birth_reduced.csv", "data/birth_reduced.csv")
urllib.request.urlretrieve("https://raw.githubusercontent.com/fredhutchio/python_intro/master/extra/smoke_complete.csv", "data/smoke_complete.csv")
```
