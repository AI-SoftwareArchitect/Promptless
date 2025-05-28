import { ApolloClient, InMemoryCache } from '@apollo/client';

const client = new ApolloClient({
  uri: 'http://localhost:4000/graphql',  // Backend GraphQL endpoint'in
  cache: new InMemoryCache(),
});

export default client;
