# Create new react / preact app
nvm use 18.18.2
npm create vite@latest
cd [project-name]

## Suggested libraries for both react and preact:
- npm install vite-plugin-replace --legacy-peer-deps ^(Yes, this is my fork, and yes, I will make it an npm package some day. Don't be a nag!)^
Used to set a value on development - I use to to replace the local config file with the production config file.

- npm install vite-plugin-static-copy
Used to create copy files on npm build into the static folder of my FastAPI / Django project.

## React only:
- npm install react-error-boundary
Used to catch errors - note that async errors are not  caught by this library.

- npm install react-use-signals
Used to provide signals to react components.

- npm install react-router-dom
Used for routing.

## Preact only:
