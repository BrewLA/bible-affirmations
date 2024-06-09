import React, { useState } from 'react';

interface AccordionProps {
  title: string;
  content: string;
}

const Accordion: React.FC<AccordionProps> = ({ title, content }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleAccordion = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="border border-gray-200 rounded-xl mb-4">
      <div 
        className="flex justify-between items-center p-4 cursor-pointer"
        onClick={toggleAccordion}
      >
        <h2 className="text-xl font-sans">{title}</h2>
        <span className="text-2xl">{isOpen ? '-' : '+'}</span>
      </div>
      {isOpen && (
        <div className="p-4 border-t border-gray-200">
          <p>{content}</p>
        </div>
      )}
    </div>
  );
};

export default Accordion;
