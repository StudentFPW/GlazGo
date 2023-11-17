import { css, styled } from "styled-components";

export const Container = styled.div`
  max-width: ${({ theme }) => theme.sizes.container.width + 30}px;
  padding: 0 15px;
  margin: 0 auto;
  width: 100%;
`
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
    color: #fff;
    background-color: ${({ theme }) => theme.colors.primary};
    &&[disabled] {
        background-color: ${({ theme }) => theme.colors.inactive};
    }
`
export const LButton = styled.button`
    ${button}
    background-color: #fff;
    border: 0.5px solid #BEBEBE;
    &&[disabled] {
        background-color: ${({ theme }) => theme.colors.inactive};
    }
`