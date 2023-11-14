import styled from "styled-components";
import Authorization from "./components/authorization/Authorization";
import { ThemeProvider } from "styled-components";
import { baseTheme } from "./styles/theme";
import GlobalStyles from "./styles/global";
import { Route, Routes } from "react-router-dom";
import Chat from "./components/chat/Chat";
import Vacancies from "./components/vacancies/Vacancies";
import NotFound from "./components/NotFound";


function App() {
  return (
    <div>
      <ThemeProvider theme={baseTheme}>
        <Wrapper>
          <Container>
            <header></header>
            <main>
              <Routes>
                <Route path="/" element={<Vacancies/>}/>
                <Route path="/authorization" element={<Authorization/>}/>
                <Route path="/chat" element={<Chat/>}/>
                <Route path="*" element={<NotFound />} />
              </Routes>
            </main>
            <footer></footer>
            <GlobalStyles />
          </Container>
        </Wrapper>
      </ThemeProvider>
    </div>
  );
}

export default App;

const Wrapper = styled.div`
  width: 390px;
  margin: 0 auto;
`
const Container = styled.div`
  max-width: ${({ theme }) => theme.sizes.container.width + 30}px;
  padding: 0 15px;
  margin: 0 auto;
  width: 100%;
`
