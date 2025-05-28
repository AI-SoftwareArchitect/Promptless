import React from 'react';
import ReactDOM from 'react-dom/client';
import { ThemeProvider, CssBaseline } from '@mui/material';
import { ApolloProvider } from '@apollo/client';
import App from './App';
import theme from './theme';
import client from './apolloClient';

ReactDOM.createRoot(document.getElementById('root')).render(
  <ApolloProvider client={client}>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <App />
    </ThemeProvider>
  </ApolloProvider>
);
