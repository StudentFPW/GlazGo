import { css, styled } from "styled-components";


export const button = css`
    height: 46px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    border: none;
`
export const FButton = styled.button`
    ${button}
    background-color: ${({ theme }) => theme.colors.primary};
    &&[disabled] {
        background-color: ${({ theme }) => theme.colors.inactive};
    }
`
export const LButton = styled.button`
    ${button}
    background-color: #fff;
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
    &&[disabled] {
        background-color: ${({ theme }) => theme.colors.inactive};
    }
`