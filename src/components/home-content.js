import React from "react";

const HomeContent = () => (
  <div className="next-steps">
    <h2 className="my-5 text-center">What can I do with Weather PI?</h2>

    <div className="row">
      <div className="col-md-5 mb-4">
        <h6 className="mb-3">
          <a
            target="_blank"
            rel="noopener noreferrer"
            href=""
          >
            <h3> <i class="fas fa-temperature-high"></i></h3>
            Track live weather data from anywhere.
          </a>
        </h6>
        <p>
          Weather pi provides a web interface for viewing your personal weather station data, your station could
          be in the same place you are in, or 1000 miles away weather PI can track as many personal stations as you want. All through a secure web portal.
        </p>
      </div>

      <div className="col-md" />

      <div className="col-md-5 mb-4">
        <h6 className="mb-3">
          <a
            target="_blank"
            rel="noopener noreferrer"
            href=""
          >
            <h3> <i class="fas fa-chart-line"></i></h3>
            Chart current and past weather data. 
          </a>
        </h6>
        <p>
         Use your weather data to make smart predictions. Weather Pi offers built in charting functionalty to view your weather data
         and to compare it too older data. 
        </p>
      </div>
    </div>

    <div className="row">
      <div className="col-md-5 mb-4">
        <h6 className="mb-3">
          <a
            target="_blank"
            rel="noopener noreferrer"
            href=""
          >
            <h3><i class="fas fa-exclamation-circle"></i></h3>
            Get Alerts
          </a>
        </h6>
        <p>
          Make your weather sensors work for you. With a few clicks you can set alerts on your web portal that will send you email when a 
          sensors reading go above or below a threshold you set. 
        </p>
      </div>

      <div className="col-md" />

      <div className="col-md-5 mb-4">
        <h6 className="mb-3">
          <a
            target="_blank"
            rel="noopener noreferrer"
            href=""
          >
            <h3><i class="fas fa-code"></i></h3>
            Use our API
          </a>
        </h6>
        <p>
          With Weather PI API you can use your data to do whatever you wish with. Creating a weather app, use our API to make import PropTypes from 'prop-types'
          more accurate. Or any project you want. 
        </p>
      </div>
    </div>
  </div>
);

export default HomeContent;
