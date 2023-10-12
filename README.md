# North Australia Water Resources Digital LIbrary

Website is published to https://nawrdl.github.io

A digital library for publications relating to water resources in Northern Australia

Note: The website expects a JSON file in the /src/statics directory. The file should contain a list of documents, each document has a set of details that describe it. It MUST have an "id" and a "title" detail. The rest can be whatever you like.

## Install the dependencies

```bash
yarn
# or
npm install
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)

```bash
quasar dev
```

### Lint the files

```bash
yarn lint
# or
npm run lint
```

### Format the files

```bash
yarn format
# or
npm run format
```

### Build the app for production

```bash
quasar build
```

### Customize the configuration

See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-vite/quasar-config-js).
