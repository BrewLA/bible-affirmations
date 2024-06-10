// ButtonWithParticles.tsx
import React from 'react';
import ParticlesBackground from '@/hooks/ParticlesBackground';

interface ModalProps {
    onClose: () => void;
  }

const ButtonWithParticles: React.FC<ModalProps> = ({ onClose }) => { 
  return (
      <div className="flex relative w-full bg-[#BC896C] justify-center items-center rounded-xl overflow-hidden">
        <button onClick={onClose} className="relative z-10 text-white px-6 py-3 transition duration-100">
          Try it out!
        </button>
        <div className="absolute z-0">
          <ParticlesBackground />
        </div>
      </div>
  );
};

export default ButtonWithParticles;
