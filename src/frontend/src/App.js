import React from 'react';
import { gql } from 'apollo-boost';
import { Query } from 'react-apollo';
import './App.css';

const App = () => (
  <div>
    <h2>Music Library</h2>
    <Query
      query={gql`
        {
          allAlbums{
            id
            name
            datePublished
            songSet{
              id
              name
              datePublished
              artist{
                id
                firstName
                lastName
                age
              }
            }
          }
        }
      `}
    >
      {({ loading, error, data }) => {
        
        if (loading) return <p className='infoMsg'>Loading, Please Wait...</p>;
        if (error) return <p className='infoMsg'>Error Fetching Data</p>;

        return data.allAlbums.map(( album ) => (
          <div >
            <ul>
              <div key={album.id} className='data'>
                <li><p>Album: {album.name}, Published At: {album.datePublished}</p>
                  <p> Includes </p>
                  {album.songSet.map(( song ) => (
                    <ul>
                      <li key={song.id}><p>Song: {song.name}, Published At: {song.datePublished} </p>
                        <ul>
                          <li key={song.artist.id}><p>Sang By: {song.artist.firstName} {song.artist.lastName}, {song.artist.age} years </p>
                          </li>
                        </ul>
                      </li>
                    </ul>
                  ))}
                </li>
              </div>
            </ul>
          </div>
        ));
      }}
    </Query> 
  </div>
);

export default App;