// import logo from '../logo.svg';
// import logo from '../svg/logo.svg'
// import logo from '../../svg/logo.svg'
// import '../App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

import React, { useRef } from "react";
import "../App.css";

const CONSTRAINTS = { video: true };

function App() {
  const videoRef = React.createRef();
  // const videoRef = useRef<HTMLVideoElement>(null);

  const startVideo = async () => {
    const stream = await navigator.mediaDevices.getUserMedia(CONSTRAINTS);
    if (videoRef && videoRef.current && !videoRef.current.srcObject) {
      videoRef.current.srcObject = stream;
    }
  };

  const endVideo = async () => {
    const stream = await navigator.mediaDevices.getUserMedia( {video: false});
    // if (videoRef && videoRef.current && !videoRef.current.srcObject) {
    videoRef.current.srcObject = stream;
      // videoRef.current.srcObject = null;
    // }
  };

  return (
    <div className="App">
      <video autoPlay ref={videoRef} />
      <button onClick={startVideo}>start</button>
      <button onClick={endVideo}>end</button>
    </div>
  );
}

export default App;
