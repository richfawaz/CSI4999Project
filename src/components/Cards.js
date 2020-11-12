import React from 'react';
import './Cards.css';
import CardItem from './CardItem';

function Cards() {
  return (
    <div className='cards'>
      <h1>Check out what weather PI lets you do </h1>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
          
            <CardItem
              src='images/img-9.jpg'
              text='Live view of current and past weather data'
              label='Live data'
              path='/sign-up'
            />
            <CardItem
              src='images/img-2.jpg'
              text='Chart current and past data trends'
              
              label='Charting' 
              
              path='/services'
            />
            
          </ul>
          <ul className='cards__items'>
            <CardItem
              src='images/img-3.jpg'
              text='Securely view your data from anywhere in the world'
              label='secure'
              path='/sign-up'
            />
            <CardItem
              src='images/img-4.jpg'
              text='Use our API to query your own data and use it as you wish'
              label='API'
              path='/sign-up'
            />
            
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards;
