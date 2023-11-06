import { createGlobalStyle } from "styled-components";

export default createGlobalStyle`
    *, *::after, *::before  {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    button {
        cursor: pointer;
    }

    button:disabled {
        cursor: default;
    }
`