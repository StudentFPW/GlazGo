import styled from "styled-components";
import Authorization from "./components/authorization/Authorization";
import { ThemeProvider } from "styled-components";
import { baseTheme } from "./styles/theme";
import GlobalStyles from "./styles/global";
import { Route, Routes } from "react-router-dom";
import Chat from "./components/chat/Chat";
import Vacancies from "./components/vacancies/Vacancies";
import NotFound from "./components/NotFound";
import Zayavka from "./components/zayavka/Zayavka";
import Vacancy from "./components/vacancy/Vacancy";
import Header from "./components/header/Header";
import * as C from "./styles/components";
import Candidates from "./components/candidates/Candidates";
import Candidate from "./components/candidate/Candidate";
import NewCandidate from "./components/candidate/NewCandidate";
import VacancyClosed from "./components/VacancyClosed";
import Registration from "./components/authorization/Registration";
import Home from "./components/Home";
import Layout from "./components/Layout";


function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Layout/>}>
          <Route index element={<Home/>}/>
          <Route path="/registration" element={<Registration/>}/>
          <Route path="/authorization" element={<Authorization/>}/>
          <Route path="/vacancies" element={<Vacancies/>}/>
          <Route path="/vacancy/:id" element={<Vacancy/>}/>
          <Route path="/zayavka" element={<Zayavka/>}/>
          <Route path="/candidates" element={<Candidates/>}/>
          <Route path="/candidate" element={<Candidate/>}/>
          <Route path="/new-candidate" element={<NewCandidate/>}/>
          <Route path="/chat" element={<Chat/>}/>
          <Route path="/vacancy-closed" element={<VacancyClosed/>}/>
          <Route path="*" element={<NotFound />} />
        </Route>
      </Routes>
    </div>
  );
}

export default App;


