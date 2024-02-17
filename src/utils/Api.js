import axios from "axios";

const url = import.meta.env.VITE_SOME_KEY;
export const GetClassification = async (query) => {
  const response = await axios.get(`${url}/predicts?query=${query}`);
  return response;
};
