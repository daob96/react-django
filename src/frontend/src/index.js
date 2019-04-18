import React from 'react';
import './index.css';
import App from './App';
import { render } from 'react-dom';
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from 'react-apollo';

// Pass your GraphQL endpoint to uri
const client = new ApolloClient({   
	uri: "http://localhost:8000/graphql" 
	// uri: "https://48p1r2roz4.sse.codesandbox.io"
});
 
const ApolloApp = AppComponent => (
  <ApolloProvider client={client}>
    <AppComponent />
  </ApolloProvider>
);
 
render(ApolloApp(App), document.getElementById('root'));
