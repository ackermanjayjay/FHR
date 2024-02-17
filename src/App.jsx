import { ChakraProvider } from "@chakra-ui/react";
import { Routes, Route } from "react-router-dom";
import Home from "./views/HomePages";
import ResultClassify from "./views/components/ResultClassification";
function App() {
  return (
    <>
      <ChakraProvider>
        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route index element={<Home />} />
          <Route path="result:query" element={<ResultClassify />} />
        </Routes>
      </ChakraProvider>
    </>
  );
}

export default App;
