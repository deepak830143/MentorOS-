import type { ButtonHTMLAttributes, ReactNode } from "react";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode;
}

export default function Button({
  children,
  className = "",
  ...props
}: ButtonProps) {
  return (
    <button
      {...props}
      className={`
        rounded-xl
        bg-blue-600
        px-5
        py-3
        font-medium
        text-white
        transition-all
        duration-300
        hover:bg-blue-700
        active:scale-95
        ${className}
      `}
    >
      {children}
    </button>
  );
}