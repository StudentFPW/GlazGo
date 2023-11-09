import styled from "styled-components";
import Authorization from "./components/authorization/Authorization";
import { ThemeProvider } from "styled-components";
import { baseTheme } from "./styles/theme";
import GlobalStyles from "./styles/global";


function App() {
  return (
    <div>
      <ThemeProvider theme={baseTheme}>
        <Wrapper>
          <Authorization/>
          <GlobalStyles />
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
