import React from 'react';
import './TimelineItem.css';

const TimelineItem = ({ data }) => (
  <div className="timeline-item">
    <div className="timeline-item-content">
      <time>{data.year}</time>
      <p>{data.title}</p>
      <span className="circle" />
    </div>
  </div>
);

export default TimelineItem;
