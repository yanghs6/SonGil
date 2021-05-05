import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './app_server/view/App';
import App2 from './app_server/view/App2';
import App_hand_pose from './app_server/view/app_hand_pose';
import App_hand_pose_deeplearning from './app_server/view/app_hand_deeplearning';
// import My_hand_pose_deeplearning from './app_server/view/my_hand_deeplearning';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>  
    {/* <App2 /> */}
    {/* <App_hand_pose /> */}
    <App_hand_pose_deeplearning />
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
