/* eslint-disable jsx-a11y/alt-text */
import React from 'react';
import * as mobilenet from '@tensorflow-models/mobilenet';
import * as tf from '@tensorflow/tfjs';

const ImageClassifier = () => {
  let net;
  // const camera = React.useRef();
  // const figures = React.useRef();
  const camera = React.createRef();
  const figures = React.createRef();
  const webcamElement = camera.current;
  let going = true;

  const run = async () => {

  };

  const startVideo = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({video: true});
    if (camera && camera.current && !camera.current.srcObject) {
      camera.current.srcObject = stream;
    }
    net = await mobilenet.load();

    const webcam = await tf.data.webcam(webcamElement, {
      resizeWidth: 220,
      resizeHeight: 227,
    });
    going = true
    while (going) {
      const img = await webcam.capture();
      const result = await net.classify(img);

      if (figures.current) {
        figures.current.innerText = `prediction : ${result[0].className} \n probability: ${result[0].probability}`;
      }
      img.dispose();

      await tf.nextFrame();

    }
  };

  const endVideo = async () => {
    // if (figures.current) {
    //   figures.current.innerText = `nothing`;
    // }
    going = false
    // const stream = await navigator.mediaDevices.getUserMedia( {video: true});
    // let vid = document.querySelector('video');
    // vid.setAttribute("ref", null)

  };
  
React.useEffect(()=> {
  run();
});

  return (
    <>
      <div
        // style="padding:5px"
        style={{padding:5+'px', fontSize:20}}
      > TFJS와 리액트 사용한 사물 인식 </div>
      <div
        style={{padding:5+'px'}}
        ref={figures}></div>
      <video
        style={{padding:5+'px'}}
        autoPlay
        playsInline
        muted={true}
        ref={camera}
        width="870"
        height="534"
      />
      <button onClick={startVideo}>start</button>
      <button onClick={endVideo}>end</button>
    </>
  );
};

export default ImageClassifier;