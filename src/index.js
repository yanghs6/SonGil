import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './app/view/App';
import App2 from './app/view/App2';
import App_hand_pose from './app/view/app_hand_pose';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>  
    {/* <App2 /> */}
    <App_hand_pose />
  </React.StrictMode>,
  document.getElementById('root')
);

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
