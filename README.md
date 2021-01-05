([Français](#api-de-rapport-dmarc))

## DMARC Report API
The DMARC Report API is exclusively focused on serving data, rather than HTML. It is a GraphQL API, chosen because of its composability, legibility and for the way it [enables both security and security automation](https://www.youtube.com/watch?v=gqvyCdyp3Nw).
It is built with the [Express webserver](https://expressjs.com/) using the [apollo-server-express middleware](https://github.com/apollographql/apollo-server/tree/main/packages/apollo-server-express), and follows the [Relay specifications for pagination](https://relay.dev/graphql/connections.htm).

#### Installing Dependencies

```shell
npm install
```

#### Running API Server

In accordance with the [12Factor app](https://12factor.net) philosophy, the server [draws it's config from the environment](https://12factor.net/config). It does based on a `.env` file that should exist in the root of the API folder which can be created with the following command, obviously modifying the test values shown to suit your setup.

```bash
cat <<'EOF' > test.env
AZURE_CONN_STRING=connection string
DATABASE=database
SUMMARIES_CONTAINER=summaries
API_CONTAINER=api
SUPER_ADMIN_TOKEN=sa-token
DMARC_REPORT_API_SECRET=test-secret
TOKEN_HASH=test-hash
DMARC_REPORT_API_TOKEN=test-token
DEPTH_LIMIT=2
COST_LIMIT=100
SCALAR_COST=1
OBJECT_COST=1
LIST_FACTOR=1
EOF
```
With that defined you can start the server with these commands.

```shell
# Run the server
npm start
```

An online IDE will be accessible at [localhost:4001/graphql](http://localhost:4001/graphql) allowing you to explore the API.

### Dev Workflow

#### Install Dev Dependencies
```shell
npm install
```

We need create the environment variables the application needs, but with some test appropriate values. We can do that by creating `test.env` in the API root directory with the following command.

```bash
cat <<'EOF' > test.env
AZURE_CONN_STRING=connection string
DATABASE=database
SUMMARIES_CONTAINER=summaries
API_CONTAINER=api
SUPER_ADMIN_TOKEN=sa-token
DMARC_REPORT_API_SECRET=test-secret
TOKEN_HASH=test-hash
DMARC_REPORT_API_TOKEN=test-token
DEPTH_LIMIT=2
COST_LIMIT=100
SCALAR_COST=1
OBJECT_COST=1
LIST_FACTOR=1
EOF
```

Finally, run the tests.

```bash
npm test
```

#### Checking Test Coverage

```shell
npm run test-coverage
```

#### Running ESLint

```shell
npm run lint
```

#### Formatting Code with Prettier
```shell
npm run prettier
```

### How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md)

### License

Unless otherwise noted, the source code of this project is covered under Crown Copyright, Government of Canada, and is distributed under the [MIT License](LICENSE).

The Canada wordmark and related graphics associated with this distribution are protected under trademark law and copyright law. No permission is granted to use them outside the parameters of the Government of Canada's corporate identity program. For more information, see [Federal identity requirements](https://www.canada.ca/en/treasury-board-secretariat/topics/government-communications/federal-identity-requirements.html).

______________________

## API de rapport DMARC

L'API du rapport DMARC est exclusivement axée sur le service des données, plutôt que sur le HTML. Il s'agit d'une API GraphQL, choisie pour sa composabilité, sa lisibilité et pour la façon dont elle [permet à la fois la sécurité et l'automatisation de la sécurité](https://www.youtube.com/watch?v=gqvyCdyp3Nw). Elle est construite avec le [serveur web Express](https://expressjs.com/) en utilisant le [middleware apollo-serveur-express](https://github.com/apollographql/apollo-server/tree/main/packages/apollo-server-express), et suit les [spécifications du relais pour la pagination](https://relay.dev/graphql/connections.htm).

#### Installer des dépendances

```shell
npm install
```

#### Exécution du serveur API

Conformément à la philosophie de [12Factor app](https://12factor.net), le serveur [tire sa configuration de l'environnement](https://12factor.net/config). Il se base sur un fichier `.env` qui devrait exister à la racine du dossier de l'API et qui peut être créé avec la commande suivante, en modifiant évidemment les valeurs de test affichées pour s'adapter à votre configuration.

```bash
cat <<'EOF' > test.env
AZURE_CONN_STRING=connection string
DATABASE=database
SUMMARIES_CONTAINER=summaries
API_CONTAINER=api
SUPER_ADMIN_TOKEN=sa-token
DMARC_REPORT_API_SECRET=test-secret
TOKEN_HASH=test-hash
DMARC_REPORT_API_TOKEN=test-token
DEPTH_LIMIT=2
COST_LIMIT=100
SCALAR_COST=1
OBJECT_COST=1
LIST_FACTOR=1
EOF
```
Une fois cela défini, vous pouvez démarrer le serveur avec ces commandes.
```shell
# Lancer le serveur
npm start
```
Un IDE en ligne sera accessible à [localhost:4001/graphql](http://localhost:4001/graphql) vous permettant d'explorer l'API.

### Flux de travail des développeurs

#### Installer des dépendances de développement
```shell
npm install
```

Nous devons créer les variables d'environnement dont l'application a besoin, mais avec des valeurs appropriées de test. Nous pouvons le faire en créant `test.env` dans le répertoire racine de l'API avec la commande suivante.

```bash
cat <<'EOF' > test.env
AZURE_CONN_STRING=connection string
DATABASE=database
SUMMARIES_CONTAINER=summaries
API_CONTAINER=api
SUPER_ADMIN_TOKEN=sa-token
DMARC_REPORT_API_SECRET=test-secret
TOKEN_HASH=test-hash
DMARC_REPORT_API_TOKEN=test-token
DEPTH_LIMIT=2
COST_LIMIT=100
SCALAR_COST=1
OBJECT_COST=1
LIST_FACTOR=1
EOF
```
Enfin, faites les tests.

```bash
npm test
```

#### Vérification de la couverture des tests

```shell
npm run test-coverage
```

#### Fonctionnement d'ESLint

```shell
npm run lint
```

#### Code de formatage plus joli
```shell
npm run prettier
```

### Comment contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md)

### Licence

Sauf indication contraire, le code source de ce projet est protégé par le droit d'auteur de la Couronne du gouvernement du Canada et distribué sous la [licence MIT](LICENSE).

Le mot-symbole « Canada » et les éléments graphiques connexes liés à cette distribution sont protégés en vertu des lois portant sur les marques de commerce et le droit d'auteur. Aucune autorisation n'est accordée pour leur utilisation à l'extérieur des paramètres du programme de coordination de l'image de marque du gouvernement du Canada. Pour obtenir davantage de renseignements à ce sujet, veuillez consulter les [Exigences pour l'image de marque](https://www.canada.ca/fr/secretariat-conseil-tresor/sujets/communications-gouvernementales/exigences-image-marque.html).
