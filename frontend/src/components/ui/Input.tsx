import type { InputHTMLAttributes } from "react";

export default function Input(
  props: InputHTMLAttributes<HTMLInputElement>
) {
  return (
    <input
      {...props}
      className="
        w-full
        rounded-xl
        border
        border-slate-300
        px-4
        py-3
        outline-none
        transition-all
        focus:border-blue-600
      "
    />
  );
}