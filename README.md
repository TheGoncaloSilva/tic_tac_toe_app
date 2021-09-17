# tic_tac_toe_app
Tic-tac-toe game (jogo do galo) using python and kivy with graphical interfaces

Install dependencies on windows wsl:
  1. Install python:
    $ sudo apt-get install python3
  2. Install Kivi
    $ sudo apt-get install python3-kivy
    2.0. Kivi website:
      https://kivy.org/doc/stable/gettingstarted/installation.html#install-pip
    2.1. Install dependecies
      $ sudo apt-get install libmtdev1
      
      # Install necessary system packages
      $ sudo apt-get install -y \
            libsdl2-dev \
            libsdl2-image-dev \
            libsdl2-mixer-dev \
            libsdl2-ttf-dev \
            libportmidi-dev \
            libswscale-dev \
            libavformat-dev \
            libavcodec-dev \
            zlib1g-dev
      
      # Install gstreamer for audio, video (optional)
      sudo apt-get install -y \
            libgstreamer1.0 \
            gstreamer1.0-plugins-base \
            gstreamer1.0-plugins-good
            
    2.2 Using Pip
      2.2.1 Install virtual environments
        $ python3 -m pip install --upgrade pip setuptools virtualenv
        $ python3 -m virtualenv kivy_venv
      2.2.2 Activate virtual environments
        2.2.2.1 Windows
          $ kivy_venv\Scripts\activate
        2.2.2.2 Bash
          $ source kivy_venv/Scripts/activate
        2.2.2.3 Linux
          $ source kivy_venv/bin/activate
      2.2.3 Install kivi
        $ python3 -m pip install kivy[base] kivy_examples
        $ python3 -m pip install kivy[full] kivy_examples -> for full dependencies
        $ pip install kivy[sdl2]
      Check the installation
        Windows:
          $ python3 kivy_venv\share\kivy-examples\demo\showcase\main.py
        Linux:
          $ python3 kivy_venv/share/kivy-examples/demo/showcase/main.py

Related example:
  https://kivy.org/doc/stable/tutorials/pong.html

# Used videos to learn about the matter
Bibliography:
  Playlist: https://www.youtube.com/watch?v=bMHK6NDVlCM
  https://www.youtube.com/watch?v=etmJGFm6hYc
  Photos: -> https://www.google.com/search?q=back+png&sxsrf=AOaemvJZK8mnhPcu6Bt04gZQNrrQWRVpJw:1631921377924&tbm=isch&source=iu&ictx=1&fir=eJkybAQNdWU6nM%252CqVyJb3dujoPY3M%252C_&vet=1&usg=AI4_-kQZZybjVgCeR_2CTC0exEfb-lxx-w&sa=X&ved=2ahUKEwjD4qDwlIfzAhUGnhQKHR8GCq0Q9QF6BAgkEAE&biw=1729&bih=1286&dpr=0.99#imgrc=0uLfDwsYfbJ6RM
          -> https://www.pngarts.com/explore/31353
