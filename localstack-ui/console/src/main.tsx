import React from "react";
import ReactDOM from "react-dom/client";
import { QueryClientProvider } from "@tanstack/react-query";
import { RouterProvider } from "@tanstack/react-router";
import { Toaster } from "sonner";
import "./styles/globals.css";
import { router } from "./router";
import { queryClient } from "./lib/queryClient";
import { CloudProvider } from "./lib/cloud-context";
import { ThemeProvider } from "./lib/theme-context";
import { I18nProvider } from "./lib/i18n";

const root = document.getElementById("root");
if (!root) throw new Error("missing #root");

ReactDOM.createRoot(root).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <ThemeProvider>
        <I18nProvider>
          <CloudProvider>
            <RouterProvider router={router} />
            <Toaster richColors closeButton position="bottom-right" />
          </CloudProvider>
        </I18nProvider>
      </ThemeProvider>
    </QueryClientProvider>
  </React.StrictMode>,
);
