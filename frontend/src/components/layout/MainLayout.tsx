import type { ReactNode } from "react";
import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

interface Props {
  children: ReactNode;
}

export default function MainLayout({ children }: Props) {
  return (
    <div className="min-h-screen bg-slate-100">
      <Sidebar />

      <div
        style={{
          marginLeft: "320px",
          minHeight: "100vh",
        }}
      >
        <Navbar />

        <main className="p-8">
          <div className="mx-6">
            {children}
          </div>
        </main>
      </div>
    </div>
  );
}