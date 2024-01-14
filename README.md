# Ranim

Manim-inspired Ren'Py template for presentation and animation. This project was initially made for AlfredPros' VN Conference 2024 talk. This template works by providing customizable screen components. These components can be combined together for the users' need.

## Usage

It is advised to run this project on Ren'Py version `7.4.x` and above.

Ren'Py version `7.5.2`/`8.0.2` and `7.5.3`/`8.0.3` are not recommended as timer-based screen made in this template would interfere with how button focus works.

Core Files : `definitions.rpy` (screen components and variables), `images/util` (images for screen components)

User Files : `script.rpy` (labels for user-specific needs), `custom_screen.rpy` (custom screens for user-specific needs)

## Contributor Note

You are free to contribute to this project. As you do, please consider the following points.

- The contribution help improve the existing components or add new components that are reasonably helpful.
- Prioritize on using screens with minimal to no additional Python displayable class for the sake of readability for non-Python programmers who will use this in the future.

## Future Plan

As of right now, I will continue to work on this as I find the need for it: such as when I am making a presentation or if someone had an interesting idea. Otherwise, there won't be much update from me apart from handling contributions to this project.
