# OpenAPI

## Tooling

### openapi-generator-cli

[Repository](https://github.com/OpenAPITools/openapi-generator-cli)

This tool is a Node wrapper around the Java JAR [openapi-generator](https://github.com/OpenAPITools/openapi-generator). It will download the correct version of the pinned JAR automatically and acts a proxy between the JAR and the user's commands when invoking this tool.

### Maintenance

#### Node Wrapper

The Node wrapper is pinned in package.json under the devDependencies. For the latest version, visit the [npmjs website for it](https://www.npmjs.com/package/@openapitools/openapi-generator-cli).

NPM and Dependabot will likely keep this up to date.

#### The JAR

The JAR version is maintained by openapitools.json. For the latest version, check the [GitHub Releases](https://github.com/OpenAPITools/openapi-generator) for the JAR. 

:warning: Unlike, the node wrapper, there is no process to keep it updated. Routinely, maintainers will need to update this pin.

## Generated Packages

All the generated packages are stored in the `gen/` folder. Nothing should manually change the code after generation.

Developers should run `npm run openapi` to generate both the frontend and backend.

### Backend

`npm run openapi-backend` command does the following:
- Cleans the folder
- Uses the [python-flask](https://github.com/OpenAPITools/openapi-generator/blob/master/docs/generators/python-flask.md) generator. Current additional properties are:
  - `packageName=chromestatus_openapi` - We generate a complete python package and this is the specified name.
- Run `pip install` again. We treat this as an independent package and it is specified in the `requirements.txt` file.

Other notes: The generator allows you to specify generating the `models` only. But for the `python-flask` generator, it will generate an incomplete setup.py in that mode. If the setup.py is incomplete, pip install will fail. As a result, we generate everything. **A future optimization would be to exclude the controller file changes via .gitignore.** Once all routes are generated by OpenAPI, it would be wise to revisit using the controllers as well.

### Frontend

`npm run openapi-frontend` command does the following:
- Cleans the folder
- Uses the [typescript-fetch](https://github.com/OpenAPITools/openapi-generator/blob/master/docs/generators/typescript-fetch.md) generator. Current additional properties are:
  - `npmName=chromestatus-openapi` - We generate a complete NPM package and this is the specified name. (That package is written in typescript and if we wanted to not use it as an independenct package, we would need typescript ourselves)
  - `withInterfaces=true` - Generate interfaces. Useful for when we migrate to typescript.
  - `supportsES6=true` - By default, it generates CommonJS ES5. That client interferes with the test framework. As a result, generate the newer es6 version. 
- Run `npm install` again. We treat this as an independent package and it is specified in the `package.json` file.


