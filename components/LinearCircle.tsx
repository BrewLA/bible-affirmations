import React from "react";

function LinearCircle() {
  return (
    <svg width="600" height="600" viewBox="0 0 600 600" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="300" cy="300" r="300" transform="matrix(-1 0 0 1 600 0)" fill="url(#paint0_linear_16246_130)"/>
        <defs>
        <linearGradient id="paint0_linear_16246_130" x1="600" y1="300" x2="0" y2="300" gradientUnits="userSpaceOnUse">
        <stop stopColor="#FFEEDA"/>
        <stop offset="1" stopColor="#BC896C" stopOpacity="0"/>
        </linearGradient>
        </defs>
    </svg>
  )
}

export default LinearCircle;