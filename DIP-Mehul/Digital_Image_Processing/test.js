let v_left_eye_inner_x = epiCycles(width / 2 + 100, 100, 0, fourier_left_eye_inner_X , left_eye_inner_time);
let v_left_eye_inner_y = epiCycles(100, height / 2 + 100, HALF_PI, fourier_left_eye_inner_Y, left_eye_inner_time);
let v_left_eye_inner = createVector(v_left_eye_inner_x.x, v_left_eye_inner_y.y);
left_eye_inner_path.unshift(v_left_eye_inner);
line(v_left_eye_inner_x.x, v_left_eye_inner_x.y, v_left_eye_inner.x, v_left_eye_inner.y);
line(v_left_eye_inner_y.x,v_left_eye_inner_y.y, v_left_eye_inner.x, v_left_eye_inner.y);
beginShape();
noFill();
for (let i = 0; i < left_eye_inner_path.length; i++) {
  vertex(left_eye_inner_path[i].x, left_eye_inner_path[i].y);
}
endShape();
const dt_left_eye_inner = TWO_PI / fourier_left_eye_inner_Y.length;
left_eye_inner_time +=dt_left_eye_inner
