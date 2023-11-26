import Authorization from "./components/authorization/Authorization";
import { Route, Routes } from "react-router-dom";
import Chat from "./components/chat/Chat";
import Vacancies from "./components/vacancies/Vacancies";
import NotFound from "./components/NotFound";
import Zayavka from "./components/zayavka/Zayavka";
import Vacancy from "./components/vacancy/Vacancy";
import Candidates from "./components/candidates/Candidates";
import Candidate from "./components/candidate/Candidate";
import NewCandidate from "./components/candidate/NewCandidate";
import VacancyClosed from "./components/VacancyClosed";
import Registration from "./components/authorization/Registration";
import Home from "./components/Home";
import Layout from "./components/Layout";
import authApi from "./services/AuthService";
import { FC, useEffect } from "react";
import { useAppDispatch } from "./hooks/redux";
import { setAuth } from "./store/redusers/authSlice";

const App: FC = () => {
  const [checkAuth] = authApi.useCheckAuthMutation()
  const dispatch = useAppDispatch()

  useEffect(() => {
    if (localStorage.getItem('accessToken')) {
      checkAuth({})
      dispatch(setAuth())
    }
  }, [])

  return (
    <Routes>
      <Route path="/" element={<Layout/>}>
        <Route index element={<Home/>}/>
        <Route path="registration" element={<Registration/>}/>
        <Route path="authorization" element={<Authorization/>}/>
        <Route path="vacancies" element={<Vacancies/>}/>
        <Route path="vacancies/:id" element={<Vacancy/>}/>
        <Route path="zayavka" element={<Zayavka/>}/>
        <Route path="vacancies/:id/candidates" element={<Candidates/>}/>
        <Route path="candidates/:id" element={<Candidate/>}/>
        <Route path="new-candidate" element={<NewCandidate/>}/>
        <Route path="chat" element={<Chat/>}/>
        <Route path="vacancy-closed" element={<VacancyClosed/>}/>
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
}

export default App;


