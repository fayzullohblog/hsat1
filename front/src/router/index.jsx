import { createBrowserRouter } from "react-router-dom";
import Home from "../pages/Home";
import RootLayout from "../layout/RootLayout";
import Admission from "../pages/Main";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/adminPanel",
    element: (
      <RootLayout>
        <Admission />
      </RootLayout>
    ),
  },
]);

export default router;
