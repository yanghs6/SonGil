/*
  - 딥러닝 이용한 손동작 인식
  - 참고 링크: https://www.youtube.com/watch?v=ZTSRZt04JkY
  - 이전 차례: app_hand.js
  - 이후 차례: x 
*/

// Import dependencies
// import React, { useRef, useState, useEffect } from "react";
// import * as tf from "@tensorflow/tfjs";
// import Webcam from "react-webcam";
// import '../App.css';
// import '../view/my_hand_deeplearning'
// import { nextFrame } from "@tensorflow/tfjs";
// // 2. TODO - Import drawing utility here
// // e.g. import { drawRect } from "./utilities";
// import {drawRect} from "controller/hand_depplearing_utilities"; 

// function App() {
//   const webcamRef = useRef(null);
//   const canvasRef = useRef(null);

//   // Main function
//   const runCoco = async () => {
//     // 3. TODO - Load network 
//     // e.g. const net = await cocossd.load();
//     // https://tensorflow-realtimemodel-example.s3.jp-tok.cloud-object-storage.appdomain.cloud/model.json
//     // https://tensorflow-realtimemodel-11.s3.jp-tok.cloud-object-storage.appdomain.cloud/model.json
//     const net = await tf.loadGraphModel('https://tensorflow-realtimemodel-11.s3.jp-tok.cloud-object-storage.appdomain.cloud/model.json')
    
//     //  Loop and detect hands
//     setInterval(() => {
//       detect(net);
//     }, 10);
//   };

//   const detect = async (net) => {
//     // Check data is available
//     if (
//       typeof webcamRef.current !== "undefined" &&
//       webcamRef.current !== null &&
//       webcamRef.current.video.readyState === 4
//     ) {
//       // Get Video Properties
//       const video = webcamRef.current.video;
//       const videoWidth = webcamRef.current.video.videoWidth;
//       const videoHeight = webcamRef.current.video.videoHeight;

//       // Set video width
//       webcamRef.current.video.width = videoWidth;
//       webcamRef.current.video.height = videoHeight;

//       // Set canvas height and width
//       canvasRef.current.width = videoWidth;
//       canvasRef.current.height = videoHeight;

//       // 4. TODO - Make Detections
//       const img = tf.browser.fromPixels(video)
//       const resized = tf.image.resizeBilinear(img, [640,480])
//       const casted = resized.cast('int32')
//       const expanded = casted.expandDims(0)
//       const obj = await net.executeAsync(expanded)
//       console.log(obj)

//       const boxes = await obj[1].array()
//       const classes = await obj[2].array()
//       const scores = await obj[4].array()
      
//       // Draw mesh
//       const ctx = canvasRef.current.getContext("2d");

//       // 5. TODO - Update drawing utility
//       // drawSomething(obj, ctx)  
//       requestAnimationFrame(()=>{drawRect(boxes[0], classes[0], scores[0], 0.8, videoWidth, videoHeight, ctx)}); 

//       tf.dispose(img)
//       tf.dispose(resized)
//       tf.dispose(casted)
//       tf.dispose(expanded)
//       tf.dispose(obj)

//     }
//   };

//   useEffect(()=>{runCoco()},[]);

//   return (mainview);
// }

// export default App;
