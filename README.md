# featuredimage

You can create featured images for your article by using Command Line Tool 'featuredimg'.

## How to use

```.text
$ pip install git+https://github.com/ryosaitok/featuredimage#egg=featuredimg
```

```.text
# This command will create an xxx image with the letters "yyy" pasted.
# It will be saved as a file called output.png.
$ featuredimg xxx -m yyy
```

```.text
# This command will create an image of the specified URL 'https://4.bp.blogspot.com/-SNILKxCoGxA/WMdTfmXnenI/AAAAAAABChM/HeJqR7MV9ZE2vXQFmdVeaZ3t6NxV6R9QwCLcB/s400/pet_nekotsugura.png' with the text "yyy" pasted.
$ featuredimg https://4.bp.blogspot.com/-SNILKxCoGxA/WMdTfmXnenI/AAAAAAABChM/HeJqR7MV9ZE2vXQFmdVeaZ3t6NxV6R9QwCLcB/s400/pet_nekotsugura.png -m This is Cat chigura
```
