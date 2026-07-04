import { ReactNode } from "react";

import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

interface MainLayoutProps {
  children: ReactNode;
}

function MainLayout({
  children,
}: MainLayoutProps) {
  return (
    <div className="flex min-h-screen bg-slate-100">

      {/* Sidebar */}

      <Sidebar />

      {/* Right Side */}

      <div className="flex flex-1 flex-col">

        {/* Navbar */}

        <Navbar />

        {/* Page Content */}

        <main className="flex-1 overflow-y-auto p-8">

          {children}

        </main>

      </div>

    </div>
  );
}

export default MainLayout;