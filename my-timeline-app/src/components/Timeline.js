import React from 'react';
import TimelineItem from './TimelineItem';
import './Timeline.css';

const Timeline = ({ items }) => (
  <div className="timeline-container">
    {items.map((item, idx) => (
      <TimelineItem data={item} key={idx} />
    ))}
  </div>
);

export default Timeline;
