import { createBrowserRouter } from "react-router-dom";
import Home from "../pages/Home";
import RootLayout from "../layout/RootLayout";
import Admission from "../pages/Amission";


const router = createBrowserRouter([
  {
    path: "/",
    element: (
      <RootLayout>
        <Home />
      </RootLayout>
    ),
  },
  {
    path: "/admission",
    element: (
      <RootLayout>
        <Admission />
      </RootLayout>
    ),
  },
]);

export default router;
