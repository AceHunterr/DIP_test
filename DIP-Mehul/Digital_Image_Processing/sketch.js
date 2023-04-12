// Coding Challenge 130.1: Drawing with Fourier Transform and Epicycles
// Daniel Shiffman
// https://thecodingtrain.com/CodingChallenges/130-fourier-transform-drawing.html
// https://youtu.be/MY4luNgGfms

// import { drawing,drawing2,nose } from "./ct";
// require('./ct.js')
console.log(drawing)

// function drawing_face_element()
// {
  // console.log("Hello")


  let x = [];
  let y = [];
  let fourierX;
  let fourierY;
  let fourierlipsX;
  let fourierlipsY;
  let fouriernoseX;
  let fouriernoseY;
  let time = 0;
  let lips_time = 0;
  let nose_time = 0;
  let path = [];
  
  let lipsX = []
  let lipsY = []
  let noseX = []
  let noseY = []
  let lipsPath = []
  let nosePath = []

  function creating_lips()
  {
    // let x = [];
    // let y = [];
    path = []
    const skip = 1;
    for (let i = 0; i < lips.length; i += skip) {
      x.push(lips[i].x);
      y.push(lips[i].y);
      lipsX.push(lips[i].x);
      lipsY.push(lips[i].y);

    }
    fourierlipsX = dft(lipsX);
    fourierlipsY = dft(lipsY);

    fourierlipsX.sort((a, b) => b.amp - a.amp);
    fourierlipsY.sort((a, b) => b.amp - a.amp);

  }

  function creating_nose()
  {
    // let x = [];
    // let y = [];
    path = []
    const skip = 1;
    for (let i = 0; i < nose.length; i += skip) {
      x.push(nose[i].x);
      y.push(nose[i].y);
      noseX.push(nose[i].x);
      noseY.push(nose[i].y);
    }
    fouriernoseX = dft(noseX);
    fouriernoseY = dft(noseY);

    fouriernoseX.sort((a, b) => b.amp - a.amp);
    fouriernoseY.sort((a, b) => b.amp - a.amp);
  }

  function setup() {
    createCanvas(1000, 1200);
    creating_lips()
    creating_nose()
    // noLoop()
    
  }

  function epiCycles(x, y, rotation, fourier , element_time) {
    for (let i = 0; i < fourier.length; i++) {
      let prevx = x;
      let prevy = y;
      let freq = fourier[i].freq;
      let radius = fourier[i].amp;
      let phase = fourier[i].phase;
      x += radius * cos(freq * element_time + phase + rotation);
      y += radius * sin(freq * element_time + phase + rotation);

      // if (dist(prevx, prevy, x, y) < 100) {
      //   stroke(255);
      //   line(prevx, prevy, x, y);
      // }

      stroke(255, 100);
      noFill();
      ellipse(prevx, prevy, radius * 2);
      stroke(255);
      line(prevx, prevy, x, y);
    }
    return createVector(x, y);
  }

  console.log(x.length)


  function drawing_element(fourierX,fourierY,element_path,element_time)
  {
    console.log("Hello")
    console.log(element_path.length)
    let vx = epiCycles(width / 2 + 100, 100, 0, fourierX , element_time);
    let vy = epiCycles(100, height / 2 + 100, HALF_PI, fourierY, element_time);
    let v = createVector(vx.x, vy.y);
    element_path.unshift(v);
    line(vx.x, vx.y, v.x, v.y);
    line(vy.x, vy.y, v.x, v.y);
    beginShape();
    noFill();
    for (let i = 0; i < element_path.length; i++) {
      vertex(element_path[i].x, element_path[i].y);
      console.log(element_path[i].x)
    }
    endShape();
    const dt = TWO_PI / fourierY.length;
    element_time += dt
    
    
  }

  function draw() {
    background(0);
    
    // console.log(x.length)
    // console.log(lipsX.length)
    // console.log(noseX.length)
    // console.log(nosePath.length)
    console.log(lipsPath.length)
    // console.log(x.length)
    // console.log(y.length+1)


    // Drawing Nose
    let v_nosex = epiCycles(width / 2 + 100, 100, 0, fouriernoseX , nose_time);
    let v_nosey = epiCycles(100, height / 2 + 100, HALF_PI, fouriernoseY, nose_time);
    let v_nose = createVector(v_nosex.x, v_nosey.y);
    nosePath.unshift(v_nose);
    line(v_nosex.x, v_nosex.y, v_nose.x, v_nose.y);
    line(v_nosey.x, v_nosey.y, v_nose.x, v_nose.y);
    beginShape();
    noFill();
    for (let i = 0; i < nosePath.length; i++) {
      vertex(nosePath[i].x, nosePath[i].y);
    }
    endShape();
    const dt_nose = TWO_PI / fouriernoseY.length;
    nose_time +=dt_nose



    // Drawing Lips 
    let v_lipsx = epiCycles(width / 2 + 100, 100, 0, fourierlipsX , lips_time);
    let v_lipsy = epiCycles(100, height / 2 + 100, HALF_PI, fourierlipsY , lips_time);
    let v_lips = createVector(v_lipsx.x, v_lipsy.y);
    lipsPath.unshift(v_lips);
    line(v_lipsx.x, v_lipsx.y, v_lips.x, v_lips.y);
    line(v_lipsy.x, v_lipsy.y, v_lips.x, v_lips.y);
    // line(vy.x, vy.y, v.x, v.y);
    // lips path
    beginShape();
    noFill();
    for (let i = 0; i < lipsPath.length; i++) {
      vertex(lipsPath[i].x, lipsPath[i].y);
    }
    endShape();
    const dt_lips = TWO_PI / fourierlipsY.length;
    lips_time += dt_lips





    // drawing_element(fouriernoseX,fouriernoseY,nosePath,nose_time)
    // drawing_element(fourierlipsX,fourierlipsY,lipsPath,lips_time)



    if (time > TWO_PI) {
      time = 0;
      path = [];
      lipsPath =[]
      nosePath = []
    }
    

  }
// }

// drawing_face_element()
// setup()


